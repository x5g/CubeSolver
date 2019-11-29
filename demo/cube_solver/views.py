import json
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from Twophase import api

def cube_solver_index(request):
    return render(request, 'CubeSolver.html')

def cube_solver_test_index(request):
    return render(request, 'CubeSolverTest.html')

def cube_solver_autotest_index(request):
    return render(request, 'autoTest.html')

def cube_index(request):
    return render(request, 'cube.html')

@csrf_exempt
def solver(request):
    state = request.GET.get("state")
    move = {'move':api.cube_solver(state)}
    return HttpResponse(json.dumps(move), content_type='application/json')