---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["55 setr.015.001.05 SwitchOrderConfirmationV05", "55.4 Message Building Blocks", "55.4.4 RelatedReference <RltdRef>", "55.4.5.21 CashSettlementDetails <CshSttlmDtls>", "55.4.5.21.1 CashInOrOut <CshInOrOut>", "55.4.5.21.1.1 CashInPaymentInstrument <CshInPmtInstrm>", "55.4.5.21.1.1.5 BankersDraftDetails <BkrsDrftDtls>", "55.4.5.21.1.1.5.4 DrawerIdentification <DrwrId>"]
file_pages: [4062]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.015.001.05"]
---

# 55.4.5.21.1.1.5.4 DrawerIdentification <DrwrId>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4062 to 4062.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4062

```text
Definition: Legal entity identification as an alternate identification for the party.
Datatype: "LEIIdentifier" on page 5395
55.4.5.21.1.1.5.4  DrawerIdentification <DrwrId>
Presence: [0..1]
Definition: Account owner that issues the cheque ordering the drawee bank to pay a specific amount,
upon demand, to the payee.
DrawerIdentification <DrwrId> contains the following elements (see "PartyIdentification139" on
page 5043 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Party <Pty> [1..1] ± 5043
   LEI <LEI> [0..1] IdentifierSet 5043
55.4.5.21.1.1.6  CashAccountDetails <CshAcctDtls>
Presence: [1..1]
Definition: Part of the investment account to or from which cash entries are made.
Impacted by: C1 "AccountElementRule"
CashAccountDetails <CshAcctDtls> contains the following InvestmentAccount60 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AccountIdentification <AcctId> [0..1] Text 4062
   Type <Tp> [0..1] ± 4062
Constraints
• AccountElementRule
Either AccountIdentification or Type must be present. Both may be present.
55.4.5.21.1.1.6.1  AccountIdentification <AcctId>
Presence: [0..1]
Definition: Unique and unambiguous identification for the account between the account owner and the
account servicer.
Datatype: "Max35Text" on page 5403
55.4.5.21.1.1.6.2  Type <Tp>
Presence: [0..1]
Definition: Account type.
Approved by the Securities SEG on 27 January 2026 setr.015.001.05 SwitchOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 4062 May 2026
```

