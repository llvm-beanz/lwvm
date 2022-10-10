set(LWVM_SOURCE_DIR ${CMAKE_CURRENT_SOURCE_DIR})
set(LWVM_BINARY_DIR ${CMAKE_CURRENT_BINARY_DIR})

if (LLVM_INCLUDE_TESTS)
  add_subdirectory(test)
  add_subdirectory(unittests)
endif()
