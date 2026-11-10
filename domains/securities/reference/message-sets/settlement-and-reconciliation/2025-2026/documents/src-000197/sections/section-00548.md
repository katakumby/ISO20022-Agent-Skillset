---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["25 sese.031.001.11 SecuritiesSettlementConditionModificationStatusAdviceV11", "26.4 Message Building Blocks"]
file_pages: [829]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.032.001.13"]
---

# 26.4 Message Building Blocks

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 829 to 829.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 829

```text
For more details, see the relevant market practice document on www.smpg.info.
C67 SettlementStatusAndMatchedRule
If settlement status/reason is used alone, then it means that the transaction is matched (if a
matching process exists in the concerned market or at the concerned account servicer).
C68 ShortLongNumberRule
ShortNumber must contain the FIN message type number of the linked message. LongNumber
must contain the XML message identifier of the linked message.
C69 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
C70 TradeDateGuideline
In addition to the settlement date (ISO 20022 mandatory), trade date is one of the 10 common
elements recommended by SMPG for equities and fixed income settlement instructions.
For more details, see the relevant market practice document on www.smpg.info.
C71 TradeDateTimeUTCRule
If Trade Date/Time is present with a time or a time + UTC indicator, then it must be the local
time of the place of trade, for example, of the stock exchange, or of the selling broker for OTC.
C72 WithLinkageRule
If Code WITH is used, then the one or more instruction which are linked become bound and
which must be executed together. Even if one single transactions/instructions/notifications can
not be executed, then all the other transactions/instructions/notifications must also be kept
pending. Therefore the use of code WITH must be limited to combine up to 2 or 3 transactions/
instructions/notifications.
26.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
26.4.1 TransactionIdentificationDetails <TxIdDtls>
Presence: [1..1]
Definition: Provides transaction type and identification information.
Impacted by: C39 "NoAccountOwnerTransactionIdentificationRule"
Approved by the Securities SEG on 27 January 2026 sese.032.001.13
SecuritiesSettlementTransactionGenerationNotificati
onV13
Settlement And Reconciliation - Maintenance 2025 - 2026 829 March 2026
```

