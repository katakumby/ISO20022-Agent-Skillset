---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000196"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["Business Examples", "IntraPositionMovementInstruction semt.013.001.07"]
content_origin: "source-transcription"
---

# IntraPositionMovementInstruction semt.013.001.07

Source: [src-000196](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart1_SettlementAndReconciliation_2025_2026_v2.docx). Locator: heading path Business Examples / IntraPositionMovementInstruction semt.013.001.07.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P953** IntraPositionMovementInstruction semt.013.001.07

**P954** Description

**P955** On the 15 January 2019, the account owner Dresdner Bank Frankfurt DRESDEFF of account 222S, requests its sub-custodian Dresdner Bank London (DRESGB2L) to move securities from the available to the restricted sub-balance. This is done with the IntraPositionMovementInstruction (semt.013.001.04).

**P956** Business Data

**P957** Transaction Identification: FRTJ123REG1

**P958** Safekeeping Account: 222S

**P959** Financial Instrument: GB0987654321

**P960** Position to be moved: 4,000,000 from the available to the restricted balance settlement 

**P961** Date: 15/01/2019

**P962** Message Instance

**P963** <IntraPosMvmntInstr>

**P964** 	<TxId>FRTJ123REG1</TxId>

**P965** 	<SfkpgAcct>

**P966** 		<Id>222S</Id>

**P967** 	</SfkpgAcct>

**P968** 	<FinInstrmId>

**P969** 		<ISIN>GB0987654321</ISIN>

**P970** 		</FinInstrmId>

**P971** 	<IntraPosDtls>

**P972** 		<SttlmQty>

**P973** 			<FaceAmt>4000000</FaceAmt>

**P974** 		</SttlmQty>

**P975** 		<SttlmDt>

**P976** 			<Dt>2019-01-15</Dt>

**P977** 		</SttlmDt>

**P978** 		<BalFr>

**P979** 		 <Tp>

**P980** 			<Cd>AVAI</Cd>

**P981** 		 </Tp>

**P982** 		</BalFr>

**P983** 		<BalTo>

**P984** 		 <Tp>

**P985** 			<Cd>RSTR</Cd>

**P986** 		</Tp>

**P987** 		</BalTo>

**P988** 	</IntraPosDtls>

**P989** </IntraPosMvmntInstr>

