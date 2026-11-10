---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000196"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["Business Examples", "SecuritiesMessageCancellationAdvice semt.020.001.07"]
content_origin: "source-transcription"
---

# SecuritiesMessageCancellationAdvice semt.020.001.07

Source: [src-000196](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart1_SettlementAndReconciliation_2025_2026_v2.docx). Locator: heading path Business Examples / SecuritiesMessageCancellationAdvice semt.020.001.07.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P1497** SecuritiesMessageCancellationAdvice semt.020.001.07

**P1498** Description

**P1499** On the 15 January 2019, the account servicer, Dresdner Bank London (DRESGB2L) informs the account owner, Dresdner Bank Frankfurt (DRESDEFF), that the previous settlement confirmation sent is cancelled. This is done with a SecuritiesMessageCancellationAdvice (semt.020.001.05).

**P1500** Business Data

**P1501** Securities Settlement Transaction Confirmation Identification: C9876XYZC2 (that is, reference for the document previously sent)

**P1502** Safekeeping Account: 222S

**P1503** Message Instance

**P1504** <SctiesMsgCxlAdvc>

**P1505** 	<Ref>

**P1506** 		<SctiesSttlmTxConfId>C9876XYZC2</SctiesSttlmTxConfId>

**P1507** 	</Ref>

**P1508** 	<SfkpgAcct>

**P1509** 		<Id>222S</Id>

**P1510** 	</SfkpgAcct>	

**P1511** </SctiesMsgCxlAdvc>

