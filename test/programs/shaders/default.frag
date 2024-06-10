#version 330 core

layout (location = 0) out vec4 fragColor;

in vec2 uv_0;
in vec3 normal;
in vec3 FragPos;


struct Light{

    vec3 position;
    vec3 Ambient;
    vec3 Diffuse;
    vec3 Specular;
};

uniform Light light;
uniform sampler2D u_texture_0;


vec3 getLight(vec3 color)
{
    vec3 Normal = normalize(normal);
    //Ambient Light

    vec3 Ambient = light.Ambient;

    //Diffuse Light
    vec3 LightDir = normalize(light.position - FragPos);
    float Diff = max(0,dot(LightDir,Normal));
    vec3 Diffuse = Diff * light.Diffuse;

    return color * (Ambient + Diffuse);


}

void main ()
{
    vec3 color = texture(u_texture_0, uv_0).rgb;
    color = getLight(color);
    fragColor = vec4(color, 1.0);
}