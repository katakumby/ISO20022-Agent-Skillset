---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.16 Miscellaneous", "35.1.16.93 SettlementTypeAndAdditionalParameters23", "35.1.16.93.9 TripartyAgentServiceProviderCollateralInstructionIdentification <TrptyAgtSvcPrvdrCollInstrId>"]
file_pages: [1645]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.16.93.9 TripartyAgentServiceProviderCollateralInstructionIdentification <TrptyAgtSvcPrvdrCollInstrId>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1645 to 1645.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1645

```text
Definition: Unique identification identifying the triparty collateral management transaction from the
triparty-agent's/service-provider's point of view.
Datatype: "Max35Text" on page 2192
35.1.16.93.9  TripartyAgentServiceProviderCollateralInstructionIdentification
<TrptyAgtSvcPrvdrCollInstrId>
Presence: [0..1]
Definition: Unique identification assigned to the instruction by the triparty-agent/service-provider.
Datatype: "Max35Text" on page 2192
35.1.16.93.10  NonceIdentification <NonceId>
Presence: [0..1]
Definition: Unambiguous identification of a random or semi-random number used once (NONCE)
generated in the frame of a cryptographic communication.
Datatype: "Max35Text" on page 2192
35.1.16.94  SettlementOrCorporateActionEvent34Choice
Definition: Choice between transaction type, corporate action event and settlement transaction.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   SecuritiesTransactionType <SctiesTxTp> [1..1] ± 1645
Or}   CorporateActionEventType <CorpActnEvtTp> [1..1] ± C13 1645
35.1.16.94.1  SecuritiesTransactionType <SctiesTxTp>
Presence: [1..1]
Definition: Identifies the type of securities transaction.
SecuritiesTransactionType <SctiesTxTp> contains one of the following elements (see
"SecuritiesTransactionType44Choice" on page 1616 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1616
Or}   Proprietary <Prtry> [1..1] ± 1618
35.1.16.94.2  CorporateActionEventType <CorpActnEvtTp>
Presence: [1..1]
Definition: Specifies the type of corporate event.
Impacted by: C13 "EventTypeRule"
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1645 March 2026
```

