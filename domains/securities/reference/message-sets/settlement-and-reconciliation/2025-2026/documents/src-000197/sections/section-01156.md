---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.16 Miscellaneous", "35.1.16.64 AdditionalParameters29", "35.1.16.64.5 ClientTripartyCollateralTransactionIdentification <ClntTrptyCollTxId>"]
file_pages: [1603]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.16.64.5 ClientTripartyCollateralTransactionIdentification <ClntTrptyCollTxId>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1603 to 1603.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1603

```text
35.1.16.64.5  ClientTripartyCollateralTransactionIdentification <ClntTrptyCollTxId>
Presence: [0..1]
Definition: Unique reference identifying the triparty collateral management transaction from the client's
point of view.
Datatype: "Max35Text" on page 2192
35.1.16.64.6  ClientCollateralInstructionIdentification <ClntCollInstrId>
Presence: [0..1]
Definition: Unique identification assigned to the instruction by the client.
Datatype: "Max35Text" on page 2192
35.1.16.64.7  TripartyAgentServiceProviderCollateralInstructionIdentification
<TrptyAgtSvcPrvdrCollInstrId>
Presence: [0..1]
Definition: Unique identification assigned to the instruction by the triparty-agent/service-provider.
Datatype: "Max35Text" on page 2192
35.1.16.65  PurposeCode7Choice
Definition: Choice between a code and or a data source scheme to determine the account type.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1603
Or}   Proprietary <Prtry> [1..1] ± 1604
35.1.16.65.1  Code <Cd>
Presence: [1..1]
Definition: Securities account purpose as an ISO 20022 code.
Datatype: "SecuritiesAccountPurposeType1Code" on page 2137
CodeName Name Definition
MARG Margin Account is used when financing is done
by the broker.
SHOR ShortSale Account is used for short sale orders.
ABRD Abroad Account is located in a financial
institution outside the country where the
transaction is taking place.
CEND Centralised Account and all its related positions are
held in one location.
DVPA CashDVP Account is used for settlement upon
delivery, or a collection on a delivery
basis.
PHYS Physical Account is used for physical domestic
safekeeping.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1603 March 2026
```

