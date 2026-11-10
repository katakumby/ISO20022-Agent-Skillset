---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.13 Identification Information", "16.1.13.7 GenericIdentification30", "16.1.13.7.3 SchemeName <SchmeNm>"]
file_pages: [880]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.13.7.3 SchemeName <SchmeNm>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 880 to 880.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 880

```text
Definition: Entity that assigns the identification.
Datatype: "Max35Text" on page 1251
16.1.13.7.3  SchemeName <SchmeNm>
Presence: [0..1]
Definition: Short textual description of the scheme.
Datatype: "Max35Text" on page 1251
16.1.13.8  SettlementTypeAndIdentification25
Definition: Overall process covering the trade and settlement transactions of financial instruments.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Payment <Pmt> [1..1] CodeSet 880
   TransactionIdentification <TxId> [1..1] Text 880
   SettlementDate <SttlmDt> [0..1] ± 880
16.1.13.8.1  Payment <Pmt>
Presence: [1..1]
Definition: Specifies how the transaction is to be settled.
Datatype: "DeliveryReceiptType2Code" on page 1207
CodeName Name Definition
FREE SeparateSettlement Settlement of the financial instrument
and cash is separate.
APMT AgainstPaymentSettlement Settlement of the financial instrument
and cash takes place in a delivery
versus payment (DVP) environment, that
is, through an International Central
Securities Depository (ICSD) or Central
Securities Depository (CSD).
16.1.13.8.2  TransactionIdentification <TxId>
Presence: [1..1]
Definition: Reference of the transaction.
Datatype: "Max35Text" on page 1251
16.1.13.8.3  SettlementDate <SttlmDt>
Presence: [0..1]
Definition: Identifies the intended settlement date.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 880 February 2026
```

