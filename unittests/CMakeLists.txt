add_custom_target(LWVMUnitTests)

function (add_lwvm_unittest test_dirname)
  add_unittest(LWVMUnitTests ${test_dirname} ${ARGN})
  set(outdir ${LWVM_BINARY_DIR}/unittests/${test_dirname}/${CMAKE_CFG_INTDIR})
  set_output_directory(${test_dirname} BINARY_DIR ${outdir} LIBRARY_DIR ${outdir})
endfunction ()

add_subdirectory(ISA)
