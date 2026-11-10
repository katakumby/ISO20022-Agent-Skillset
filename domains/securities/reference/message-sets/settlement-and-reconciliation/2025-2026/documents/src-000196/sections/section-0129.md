---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000196"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["Business Examples", "SecuritiesSettlementTransactionModificationRequest sese.038.001.11"]
content_origin: "source-transcription"
---

# SecuritiesSettlementTransactionModificationRequest sese.038.001.11

Source: [src-000196](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart1_SettlementAndReconciliation_2025_2026_v2.docx). Locator: heading path Business Examples / SecuritiesSettlementTransactionModificationRequest sese.038.001.11.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P3154** SecuritiesSettlementTransactionModificationRequest sese.038.001.11

**P3155** Description

**P3156** On the 14 January 2019, Dresdner Bank Frankfurt (DRESDEFF), the account owner, instructs their sub-custodian Dresdner Bank London (DRESGB2L) to modify a previously sent delivery against payment securities instruction in favour of their customer JP Morgan Investment GMBH Frankfurt (MGTCDE55). This is done through a Securities Settlement Transaction Modification Request (sese.038.001.05).

**P3157** Business Data

**P3158** Account Owner Transaction Identification : FRTJ123DEL

**P3159** Securities Movement Type: Delivery

**P3160** Payment: against payment

**P3161** Settlement Date: 15/01/2019

**P3162** Safekeeping Account: 222S

**P3163** Update Type: Modification

**P3164** Securities Transaction Type is modified to PAIR

**P3165** Message Instance

**P3166** <SctiesSttlmTxModReq>

**P3167** 	<ModfdTxDtls>

**P3168** 		 <AcctOwnrTxId>

**P3169** 	         	<TxId>FRTJ123DEL</TxId>

**P3170** 	       	   	<SctiesMvmntTp>DELI</SctiesMvmntTp>

**P3171**        	   		<Pmt>APMT</Pmt>

**P3172** 		</AcctOwnrTxId>

**P3173** 		<SfkpgAcct>

**P3174**  		    <Id>222S</Id>

**P3175** 		</SfkpgAcct>

**P3176** 	</ModfdTxDtls>

**P3177** 	<UpdTp>

**P3178** 		<Mod>

**P3179** 		     <SttlmParams>

**P3180** 			     <SctiesTxTp>

**P3181**  				    <Cd>PAIR</Cd>

**P3182** 			</SctiesTxTp>

**P3183** 		     </SttlmParams>

**P3184** 		</Mod>

**P3185** 	</UpdTp>

**P3186** </SctiesSttlmTxModReq>	

