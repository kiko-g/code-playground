function scanner(string) {
  let index = 0;
  let tokens = [];

  while (index < string.length) {
    switch (string[index]) {
      case LPAR:
      case RPAR:
      case MUL:
      case DIV:
      case PLUS:
      case SUB:
      case EQ:
      case SEMICOLON:
        tokens.push(string[index]);
        break;

      case INT:
      case VAR:
        let increment = 1;
        let token = string[index];

        while (string[index + increment] == INT || string[index + increment] == VAR) {
          increment++; //look further
          token += string[index + increment]; //add next char
        }

        tokens.push(token);
        break;

      default:
        console.log('Character ' + string[index] + ' does not belong to the language');
        break;
    }

    index++;
  }

  return tokens; //return array of tokens
}