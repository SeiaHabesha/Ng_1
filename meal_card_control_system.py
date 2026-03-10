{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOG2RlKWtLIx3xUCJyHtOIa",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/SeiaHabesha/Ng_1/blob/main/logic2.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "bD8vLc8jWWHM"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "collapsed": true,
        "id": "wjTC_4oHR1X9"
      },
      "outputs": [],
      "source": [
        "import datetime\n",
        "import json\n",
        "\n",
        "\n",
        "\n",
        "# List of authorized student IDs\n",
        "valid_student=[2533,2634,2735,2836,2937]\n",
        "\n",
        "\n",
        "# Initialize or load existing records from the JSON file (Data Persistence)\n",
        "try:\n",
        "    with open(\"meal_records.json\", \"r\") as f:\n",
        "        eaten_today = json.load(f)\n",
        "\n",
        "       # Convert dictionary keys back to integers after loading from JSON\n",
        "\n",
        "        eaten_today = {int(k): v for k, v in eaten_today.items()}\n",
        "except (FileNotFoundError, json.JSONDecodeError):\n",
        "  eaten_today={}\n",
        "\n",
        "def check_meal():\n",
        "  while True:\n",
        "\n",
        "    stud_input=input(\"Enter meal ID: \")\n",
        "    if stud_input.lower()==\"exit\":\n",
        "      break\n",
        "    try:\n",
        "      stud_input=int(stud_input)\n",
        "    except ValueError:\n",
        "      print(\"Invalid input. Please enter a valid meal ID or 'exit' to quit.\")\n",
        "      continue\n",
        "\n",
        "    if stud_input not in valid_student:\n",
        "      print(\"Invalid meal ID. Please enter a valid meal ID.\")\n",
        "      continue\n",
        "\n",
        "# Get the current date to distinguish between yesterday and today\n",
        "\n",
        "    today = datetime.datetime.now().strftime(\"%Y-%m-%d\")\n",
        "\n",
        "    # Check if the student has already eaten\n",
        "\n",
        "    if stud_input in eaten_today:\n",
        "      last_record=eaten_today[stud_input]\n",
        "\n",
        "      # Logic to prevent double-eating on the same day\n",
        "\n",
        "      if today in last_record:\n",
        "         last_meal=eaten_today[stud_input]\n",
        "\n",
        "\n",
        "      print(f\"You have already eaten today at{last_record}.\")\n",
        "      continue\n",
        "\n",
        "    # Record the new meal with full date and time\n",
        "\n",
        "    else:\n",
        "      now_full= datetime.datetime.now().strftime(\"%Y-%m-%d %H:%M:%S\")\n",
        "      eaten_today[stud_input] = now_full\n",
        "    # Save the updated dictionary to the JSON file immediately\n",
        "\n",
        "      with open(\"meal_records.json\", \"w\") as f:\n",
        "            json.dump(eaten_today, f, indent=4)\n",
        "\n",
        "      print(\"Meal ID  alowed.\")\n",
        "\n",
        "if __name__ == \"__main__\":\n",
        "\n",
        "\n",
        "  check_meal()\n",
        "\n",
        "\n",
        "\n",
        ""
      ]
    }
  ]
}
