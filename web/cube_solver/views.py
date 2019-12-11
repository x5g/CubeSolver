import requests, json
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from Twophase import api

def cube_solver_index(request):
    return render(request, 'CubeSolver.html')

def cube_solver_test_index(request):
    return render(request, 'CubeSolverTest.html')

def cube_index(request):
    return render(request, 'cube.html')

def deepcube_index(request):
    return render(request, 'DeepCube.html')

@csrf_exempt
def solver(request):
    state = request.GET.get("state")
    move = {'move':api.cube_solver(state)}
    return HttpResponse(json.dumps(move), content_type='application/json')


url = 'http://deepcube.igb.uci.edu'

# @csrf_exempt
# def initState(request):
#     r = requests.post(url + '/initState', data={})
#     key = json.loads(r.text)    # 这一步将返回值转成json
#     return HttpResponse(json.dumps(key), content_type='application/json')

@csrf_exempt
def initState(request):
    import os
    with open(os.path.abspath(os.path.dirname(os.getcwd())+os.path.sep+".") + '/static/DeepCube/initState.json', 'r') as f:
        result = json.load(f)
    return HttpResponse(json.dumps(result), content_type='application/json')

@csrf_exempt
def solve(request):
    state = request.POST.get("state")
    r = requests.post(url + '/solve', data={'state': state})
    key = json.loads(r.text)    # 这一步将返回值转成json
    return HttpResponse(json.dumps(key), content_type='application/json')
