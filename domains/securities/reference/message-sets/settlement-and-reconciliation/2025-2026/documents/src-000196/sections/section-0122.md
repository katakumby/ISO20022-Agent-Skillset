---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000196"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["Business Examples", "SecuritiesSettlementConditionsStatusAdvice sese.031.001.11"]
content_origin: "source-transcription"
---

# SecuritiesSettlementConditionsStatusAdvice sese.031.001.11

Source: [src-000196](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart1_SettlementAndReconciliation_2025_2026_v2.docx). Locator: heading path Business Examples / SecuritiesSettlementConditionsStatusAdvice sese.031.001.11.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P2422** SecuritiesSettlementConditionsStatusAdvice sese.031.001.11

**P2423** Description

**P2424** On the 8 January 2019, Dresdner Bank London (DRESGB2L) advises its customer Dresdner Bank Frankfurt (DRESDEFF) on the status of a previous modification request. This is done through a SecuritiesSettlementConditionsModificationStatusAdvice (sese.031.001.07).

**P2425** Business Data

**P2426** Requested Reference: FRTJ123REC2HOLD

**P2427** Securities Movement Type: receive

**P2428** Payment: payment

**P2429** Safekeeping Account: 222S

**P2430** Requested Detail - Hold Indicator: false

**P2431** Processing Status (no reason): rejected

**P2432** Message Instance

**P2433** <SctiesSttlmCondModStsAdvc>

**P2434** 	<ReqRef>

**P2435** 		<Id>FRTJ123REC2HOLD</Id>

**P2436** 	</ReqRef>

**P2437** 	<SfkpgAcct>

**P2438** 		<Id>222S</Id>

**P2439** 	</SfkpgAcct>

**P2440** 	<ReqDtls>

**P2441** 		<Ref/>

**P2442** 		<HldInd>

**P2443** 		<Ind>false</Ind></HldInd>

**P2444** 	</ReqDtls>

**P2445** 	<PrcgSts>

**P2446** 		<Rjctd>

**P2447** 			<NoSpcfdRsn>NORE</NoSpcfdRsn>

**P2448** 		</Rjctd>

**P2449** 	</PrcgSts>

**P2450** </SctiesSttlmCondModStsAdvc>

