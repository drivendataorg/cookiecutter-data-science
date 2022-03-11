# Adding a DAG to run batch predictions

After you created the necessary infrastructure by following [these steps](../infrastructure/README.md), you can 
create a DAG using the template in this directory.

1. clone the Airflow DAGs repo:  
`git clone https://github.com/contentful/data-airflow-dags`
2. Adapt the python file in this directory to your wishes or just copy it directly into the dags folder:  
`cp {{cookiecutter.repo_name}}_dag.py <path_to_dag_repo>/dags/<subfolder>/`
3. create a branch, commit, and make a PR. After it is accepted and merged it should be available on airflow. 