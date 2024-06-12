#version 120
varying vec3 tex_coords;
uniform samplerCube skybox;

void main()
{
    gl_FragColor = textureCube(skybox, tex_coords);
}
