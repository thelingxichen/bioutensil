zcat $biodb_human_ens75_gene_psl_idx_bgz | cut -f9,10,14,16,17 | awk '{print $3"\t"$4"\t"$5"\t"$2"\t"$1}' > ens75.hg19.gene.f10.sorted.bed
