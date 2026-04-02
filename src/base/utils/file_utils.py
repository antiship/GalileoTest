import configparser
import json
import os


class FileUtils:
    @staticmethod
    def get_parser(config):
        parser = configparser.ConfigParser()
        with open(config, mode='r', buffering=-1, closefd=True):
            parser.read(config)
            return parser

    @staticmethod
    def save_into_file(result, file):

        with open(file, "r+") as f:
            s = f.read()
            f.seek(0)
            f.write(str(result) + "\n" + str(s))

    @staticmethod
    def save_allure_environment(env_dir, env_var):
        if not os.path.exists(env_dir):
            os.makedirs(env_dir)
        with open(os.path.join(env_dir + "environment.properties"), "w+") as f:
            f.write(env_var)

    @staticmethod
    def save_allure_executor(env_dir, executor):
        if not os.path.exists(env_dir):
            os.makedirs(env_dir)
        with open(os.path.join(env_dir + "executor.json"), "w+") as f:
            f.write(json.dumps(executor))
