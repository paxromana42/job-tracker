#include <webgpu/webgpu.h>
#include <iostream>

int main() {
    // Create a descriptor
    WGPUInstanceDescriptor desc{};
    desc.nextInChain = nullptr;

    // Create the WebGPU instance
    WGPUInstance instance = wgpuCreateInstance(&desc);
    if (!instance) {
        std::cerr << "Failed to init WebGPU instance" << std::endl;
        return 1;
    }

    std::cout << "Hello WebGPU! Instance: " << instance << std::endl;

    // Release the instance
    wgpuInstanceRelease(instance);
    return 0;
}
