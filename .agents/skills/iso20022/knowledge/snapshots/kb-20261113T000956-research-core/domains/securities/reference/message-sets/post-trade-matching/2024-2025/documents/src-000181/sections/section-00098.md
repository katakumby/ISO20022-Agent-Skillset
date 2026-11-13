---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["3 setr.027.001.05 SecuritiesTradeConfirmationV05", "3.4 Message Building Blocks", "3.4.19 OtherBusinessParties <OthrBizPties>", "3.4.19.5 QualifiedForeignIntermediary <QlfdFrgnIntrmy>"]
file_pages: [129]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.027.001.05"]
---

# 3.4.19.5 QualifiedForeignIntermediary <QlfdFrgnIntrmy>

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 129 to 129.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 129

```text
TripartyAgent <TrptyAgt> contains the following elements (see "PartyIdentificationAndAccount154"
on page 476 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 476
   SafekeepingAccount <SfkpgAcct> [0..1] Text 477
   CashAccount <CshAcct> [0..1] ± 477
   ProcessingIdentification <PrcgId> [0..1] Text 477
   AdditionalInformation <AddtlInf> [0..1] ± C2 477
   AlternateIdentification <AltrnId> [0..1] ± 478
3.4.19.5  QualifiedForeignIntermediary <QlfdFrgnIntrmy>
Presence: [0..1]
Definition: Foreign Financial Institution which has been authorised by local authorities to act as account
management institution in the country.
QualifiedForeignIntermediary <QlfdFrgnIntrmy> contains the following elements (see
"PartyIdentificationAndAccount151" on page 402 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 402
   AlternateIdentification <AltrnId> [0..1] ± 402
   SafekeepingAccount <SfkpgAcct> [0..1] Text 403
   ProcessingIdentification <PrcgId> [0..1] Text 403
   AdditionalInformation <AddtlInf> [0..1] ± C2 403
3.4.20 TwoLegTransactionDetails <TwoLegTxDtls>
Presence: [0..1]
Definition: Specifies a transaction that the trading parties are agreeing to repurchase, sell back or return
the same or similar securities at a later time.
The two leg transaction details defines the closing leg conditions of a two leg transaction. It is also used
to define the anticipated closing leg conditions at the time of opening the closed-end transaction.
Approved by the Securities SEG on 13 February 2025 setr.027.001.05 SecuritiesTradeConfirmationV05
Post Trade Matching - Maintenance 2024 - 2025 129 February 2025
```

