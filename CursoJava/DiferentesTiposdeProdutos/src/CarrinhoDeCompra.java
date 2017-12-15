import java.util.HashMap;
import java.util.Map;
import java.util.Set;
public class CarrinhoDeCompra {

	// Hashmap de produtos
	Map <Produto,Integer> itenscompra;
	
	
	// metodo que adicona produtos ao carrinho
	public void adicionaProduto(Produto produto,int quantidade){
		
		itenscompra = new HashMap<Produto,Integer>();
		
		for (int i=0; i < itenscompra.size(); i++){
			
			if(itenscompra.containsKey(produto)){
				int valor =itenscompra.get(quantidade)+1;
				itenscompra.put(produto, valor);
				
			}else{
				itenscompra.put(produto, 1);
			}	
			
		}
	}
	
	// método que remove produto 
	
	public void removeProduto(Produto produto, int quantidade ,int retirar){
		for (int i = 0; i < itenscompra.size(); i++){
				if(itenscompra.containsKey(produto)){ 
					int valor = itenscompra.get(quantidade)-retirar;
					itenscompra.put(produto, valor);
				if (quantidade == retirar){
					itenscompra.remove(produto);
				}
			}
		}
		
	}
	
	// método que calcula valor total da compra
	
	public void valorTotal(Produto produto){
		float precototal=0;
		Set<Produto> produtos=itenscompra.keySet();
		for (Produto p : produtos) {
		    precototal=precototal + p.getPreço();
		}
	}
}
