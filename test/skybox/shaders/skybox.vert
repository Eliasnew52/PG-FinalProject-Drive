#version 120
varying vec3 tex_coords;

void main()
{
    gl_Position = gl_ProjectionMatrix * gl_ModelViewMatrix * gl_Vertex;
    tex_coords = vec3(gl_Vertex) * vec3(1, 1, -1);
}
