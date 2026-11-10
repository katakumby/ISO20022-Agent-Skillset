---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["72 semt.027.001.01 SecuritiesSettlementTransactionQueryResponseV01", "72.4 Message Building Blocks", "72.4.3 Transactions <Txs>", "72.4.3.4 Transaction <Tx>", "72.4.3.4.18 TransactionDetails <TxDtls>", "72.4.3.4.18.11 ConditionalSecuritiesDelivery <CondlSctiesDlvry>"]
file_pages: [2550]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.027.001.01"]
---

# 72.4.3.4.18.11 ConditionalSecuritiesDelivery <CondlSctiesDlvry>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2550 to 2550.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2550

```text
Definition: Primary market or country where a security is issued by the issuer or its agent.
Impacted by: C9 "Country"
Datatype: "CountryCode" on page 3234
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
72.4.3.4.18.11  ConditionalSecuritiesDelivery <CondlSctiesDlvry>
Presence: [0..1]
Definition: Specifies whether the transaction is under Conditional Securities Delivery (CoSD).
Datatype: One of the following values must be used (see "YesNoIndicator" on page 3323):
• Meaning When True: Yes
• Meaning When False: No
72.4.3.4.18.12  SettlementQuantity <SttlmQty>
Presence: [1..1]
Definition: Total quantity of financial instrument to be settled.
SettlementQuantity <SttlmQty> contains one of the following elements (see
"FinancialInstrumentQuantity1Choice" on page 2953 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Unit <Unit> [1..1] Quantity 2954
Or   FaceAmount <FaceAmt> [1..1] Amount 2954
Or}   AmortisedValue <AmtsdVal> [1..1] Amount 2954
72.4.3.4.18.13  SettledQuantity <SttldQty>
Presence: [0..1]
Definition: Quantity of financial instrument effectively settled and which will be delivered to/received
from the account owner's securities account. It may differ from the instructed settlement quantity based
on market tolerance level.
SettledQuantity <SttldQty> contains one of the following elements (see
"FinancialInstrumentQuantity1Choice" on page 2953 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Unit <Unit> [1..1] Quantity 2954
Or   FaceAmount <FaceAmt> [1..1] Amount 2954
Or}   AmortisedValue <AmtsdVal> [1..1] Amount 2954
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.027.001.01
SecuritiesSettlementTransactionQueryResponseV0
1
Target2-Securities 2550 August 2026
```

