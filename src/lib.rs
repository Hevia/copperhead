use std::fs;
use pyo3::prelude::*;
use pyo3::wrap_pyfunction;

/// Open a file & read a file as a string
#[pyfunction]
fn read_file(filename: String) -> PyResult<String>{
     Ok(fs::read_to_string(filename).expect("Couldn't find file at path!"))
}

#[pymodule]
fn copperhead(_py: Python<'_>, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(read_file, m)?)?;
    Ok(())
}
