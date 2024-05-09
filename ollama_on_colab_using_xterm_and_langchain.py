# -*- coding: utf-8 -*-
"""Ollama_on_Colab_using_xterm and langchain.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1CwkcgqRSwQxUOr3-pXceUHUijrvWT5jz

# Ollama running on Google Colab T4 free using langchain community

*   Firstly, install langchain packages
*   Then install colab-xterm
*   Then load colab-xterm
*   Then run xterm to open a terminal inside a cell
*   Then write the installation code for Ollama inside the xterm terminal
*   Then, start Ollama server and pull llama2 model
*   Then, go outside of the xterm
*   Then, import packages from langchain community
*   Then, load llama2 model via Ollama
*   lastly, invoke llama2 model by a prompt thatbhits the Ollama server. You can look into the xterm to see wheether status 200 is seen, that means the hit is correct.

Install Langchain tools
"""

!pip install langchain
!pip install langchain-core
!pip install langchain-community

"""Install Colab xterm"""

!pip install colab-xterm

"""Load colabxterm"""

# Commented out IPython magic to ensure Python compatibility.
# %load_ext colabxterm

"""Start the xterm by using **%xterm**

Next, install Ollama by typing below inside xterm

based on https://github.com/ollama/ollama

curl -fsSL https://ollama.com/install.sh | sh

Next, Start Ollama server and also Pull any model For example Llama3

ollama serve & ollama run llama2
"""

# Commented out IPython magic to ensure Python compatibility.
# %xterm

"""Import Ollama from langchain community

load llama2 model which was pulled above and available for current Ollama server
"""

from langchain_community.llms import Ollama

llm = Ollama(model="llama2")

"""Provide your prompt inside the llm.invoke("    Your prompt     ")"""

llm.invoke("Write a poem on rose")

llm.invoke("Write a c code in for factorial")