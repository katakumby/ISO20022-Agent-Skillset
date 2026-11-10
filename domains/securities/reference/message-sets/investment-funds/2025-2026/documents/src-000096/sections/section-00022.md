---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["3 acmt.002.001.08 AccountDetailsConfirmationV08", "3.4 Message Building Blocks", "3.4.4 ConfirmationDetails <ConfDtls>", "3.4.4.2 AccountApplicationIdentification <AcctApplId>"]
file_pages: [45]
content_origin: "source-text-extraction"
mentioned_message_ids: ["acmt.002.001.08"]
---

# 3.4.4.2 AccountApplicationIdentification <AcctApplId>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 45 to 45.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 45

```text
ConfirmationType <ConfTp> contains one of the following elements (see "ConfirmationType1Choice"
on page 4323 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4324
Or}   Proprietary <Prtry> [1..1] ± 4324
3.4.4.2  AccountApplicationIdentification <AcctApplId>
Presence: [0..1]
Definition: Unique and unambiguous identifier of the account opening or modification instruction at
application level.
Datatype: "Max35Text" on page 5403
3.4.4.3  ClientReference <ClntRef>
Presence: [0..1]
Definition: Unique and unambiguous identification of a transaction, for example, a transfer, as assigned
by the investor or account owner.
Datatype: "Max35Text" on page 5403
3.4.4.4  CounterpartyReference <CtrPtyRef>
Presence: [0..1]
Definition: Unambiguous identification of the transaction, for example, a transfer, as allocated by the
counterparty.
CounterpartyReference <CtrPtyRef> contains the following elements (see "AdditionalReference13"
on page 4546 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reference <Ref> [1..1] Text 4546
   ReferenceIssuer <RefIssr> [0..1] ± 4546
   MessageName <MsgNm> [0..1] Text 4547
3.4.4.5  ExistingAccountIdentification <ExstgAcctId>
Presence: [0..*]
Definition: Account to which the account opening is related.
ExistingAccountIdentification <ExstgAcctId> contains the following elements (see "Account23" on
page 4325 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AccountIdentification <AcctId> [1..1] Text 4325
   RelatedAccountDetails <RltdAcctDtls> [0..1] ± 4325
Approved by the Securities SEG on 27 January 2026 acmt.002.001.08 AccountDetailsConfirmationV08
Investment Funds - Maintenance 2025 - 2026 45 May 2026
```

