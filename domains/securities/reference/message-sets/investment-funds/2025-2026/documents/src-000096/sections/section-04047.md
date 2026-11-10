---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.2 Message Datatypes", "66.2.2 CodeSet", "66.2.2.207 SettlementTransactionCondition11Code"]
file_pages: [5363]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.2.2.207 SettlementTransactionCondition11Code

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 5363 to 5363.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5363

```text
CodeName Name Definition
SUBS Subscription Settlement of subscriptions or
subscription legs of a switch transaction.
WTHP WithdrawalSavingsPlan Settlement of withdrawals from a savings
plan.
CORP CorporateAction Settlement of corporate actions.
66.2.2.207  SettlementTransactionCondition11Code
Definition: Specifies the conditions under which a order/trade is to be settled.
Type: CodeSet
CodeName Name Definition
NOMC NoAutomaticMarketClaim No market claim should be automatically
generated.
66.2.2.208  SignatureType1Code
Definition: Type of signature form.
Type: CodeSet
CodeName Name Definition
ORIG Original The investor's written signature is
required. Can also be known as physical
or wet signature.
DIGI Digital A technical signature that includes
algorithms and private key and public
key information. Used to sign and verify
the contents of a message.
ELEC Electronic A copy of a physical or original signature
in an electronic format.
NONE None There is no signature required in any
form.
66.2.2.209  SignatureType2Code
Definition: Type of signature.
Type: CodeSet
CodeName Name Definition
DIGI Digital Technical signature that includes
algorithms and private key and public
key information. Used to sign and verify
the contents of a message.
ELEC Electronic Copy of a physical or original signature
in an electronic format.
NONE None No signature.
ORIG Original Written signature. May also be known as
a physical or wet signature.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5363 May 2026
```

