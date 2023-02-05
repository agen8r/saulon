while true
  % Lista de delimitadores comuns
  delimiters = {"\t", ",", ";", "|"};

% Abre o arquivo .csv
  fid = fopen("CovidNumerico.csv");

% Inicializa a variável para armazenar o delimitador
  delimiter = "";

% Loop através da lista de delimitadores
  for i = 1:length(delimiters)

  % Verifica se o arquivo pode ser lido usando o delimitador atual
    try
      data = dlmread("CovidNumerico.csv", delimiters{i}, 1, 0);
      delimiter = delimiters{i};
      break;
    catch
    % Continua para o próximo delimitador se a leitura falhar
      continue;
    end
  end

% Fecha o arquivo
fclose(fid);

% Verifica se o delimitador foi encontrado
if isempty(delimiter)
  disp("Não foi possível identificar o delimitador do arquivo .csv");
  return;
else
  % Lê o título das colunas do arquivo usando o delimitador identificado
  fid = fopen("CovidNumerico.csv");
  titulos = strsplit(fgetl(fid), delimiter);
  fclose(fid);

  % Exibe as colunas disponíveis para filtrar
  clc;
  disp("Colunas disponíveis para filtrar:");
  disp(" ");
  for i = 1:length(titulos)
    disp(sprintf("%d - %s", i, titulos{i}));
  end
end
  % Pergunta ao usuário qual coluna deseja filtrar
    disp(" ");
  coluna = input("Qual coluna deseja filtrar? ");
      if coluna < 1 || coluna > 7
      disp("Coluna inválida. Tente novamente.")
      break
    endif
  % Pergunta ao usuário quantas vezes o filtro deve ser aplicado
      disp(" ");
  passadas = input("Quantas vezes deseja aplicar o filtro de Savitsky-Golay? ");
  % Aplicando o filtro de Savitsky-Golay
  largura = 3;
  ordem_polinomio = 1;
  if mod(largura, 2) == 0 % verifica se o tamanho do filtro é ímpar
    largura = largura + 1; % se não for, aumenta em 1 para torná-lo ímpar
  end
  filtrado = sgolayfilt(data(:,coluna), ordem_polinomio, largura);
  for i=1:passadas-1
    filtrado = sgolayfilt(filtrado, ordem_polinomio, largura);
  end
  % Plotagem dos dados originais e dos dados filtrados
  figure;
  plot(data(:,coluna), "b", "LineWidth", 2, "DisplayName", sprintf("Dados originais - %s", titulos{coluna}));
  hold on;
  plot(filtrado, "r", "LineWidth", 2, "DisplayName", sprintf("Dados filtrados - %s", titulos{coluna}));
  legend("show");
  xlabel("Tempo");
  ylabel("Valor");
  title(sprintf("Filtro de Savitsky-Golay aplicado %d vezes na coluna %s", passadas, titulos{coluna}));
  % Pergunta ao usuário se deseja finalizar o programa
  finalizar = input("Deseja finalizar o programa? (y/n) ", "s");
  if strcmpi(finalizar, "y") || strcmpi(finalizar, "Y")  %comparando strings independentemente da capitalização
    break;
  end
end
