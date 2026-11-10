---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000196"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["Business Examples", "SecuritiesSettlementConditionsModificationRequest sese.030.001.10"]
content_origin: "source-transcription"
---

# SecuritiesSettlementConditionsModificationRequest sese.030.001.10

Source: [src-000196](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart1_SettlementAndReconciliation_2025_2026_v2.docx). Locator: heading path Business Examples / SecuritiesSettlementConditionsModificationRequest sese.030.001.10.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P2401** SecuritiesSettlementConditionsModificationRequest sese.030.001.10

**P2402** Description

**P2403** On the 07 January 2019, Dresdner Bank Frankfurt (DRESDEFF), the account owner, instructs their sub-custodian Dresdner Bank London (DRESGB2L) to release a receipt that was previously sent and put on hold. This is done through the SecuritiesSettlementConditionsModificationRequest (sese.030.001.07).

**P2404** Business Data

**P2405** Safekeeping Account: 222S

**P2406** Transaction reference to be modified: FRTJ123REC2

**P2407** Hold indicator: false

**P2408** Message Instance

**P2409** <SctiesSttlmCondsModReq>

**P2410** 	<SfkpgAcct>

**P2411** 		<Id>222S</Id>

**P2412** 	</SfkpgAcct>

**P2413** 	<ReqDtls>

**P2414** 		<Ref>

**P2415** 			<AcctOwnrTxId>FRTJ123REC2</AcctOwnrTxId>

**P2416** 		</Ref>

**P2417** 		<HldInd>

**P2418** 		<Ind>false</Ind>

**P2419** 		</HldInd>

**P2420** 	</ReqDtls>

**P2421** </SctiesSttlmCondsModReq>

