---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["47 setr.007.001.05 SubscriptionBulkOrderV05", "47.4 Message Building Blocks", "47.4.4 BulkOrderDetails <BlkOrdrDtls>", "47.4.4.8 IndividualOrderDetails <IndvOrdrDtls>", "47.4.4.8.16 TransactionOverhead <TxOvrhd>", "47.4.4.8.16.3 IndividualTax <IndvTax>", "47.4.4.8.16.3.5 ExemptionReason <XmptnRsn>", "47.4.4.8.16.3.5.2 Proprietary <Prtry>"]
file_pages: [2607]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.007.001.05"]
---

# 47.4.4.8.16.3.5.2 Proprietary <Prtry>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 2607 to 2607.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2607

```text
CodeName Name Definition
RIAN RothIRANonPrototype Roth Individual Retirement Account
(IRA) Non-Prototype. Account is a tax-
deferred retirement account based on
the reverse principle of a traditional IRA.
Retirement contributions are taxed
upfront, but withdrawals may be made
tax-free when a certain age is reached,
provided the Roth IRA has been set up
for a certain period of time (required for
US).
RCRF RothConversionIRAFundPrototype Roth Conversion Individual Retirement
Account (IRA) Fund Prototype. Account
is a retirement account established when
a party switches from a regular IRA
( required for US).
RCIP RothConversionIRANonPrototype Roth Conversion Individual Retirement
Account (IRA) Non-Prototype. Account is
a retirement account established when a
party switches from a Regular IRA
(required for US).
EIFP EducationIRAFundPrototype Education Individual Retirement Account
Fund Prototype (also known as an
Education Savings Account). Account is
a savings plan open to anyone under the
age of 18. When the account owner
withdraws money to pay for qualified
higher education expenses, the
withdrawals are generally tax-free
(required for US).
EIOP EducationIRANonPrototype Education Individual Retirement Account
Non-Prototype (also known as an
Education Savings Account). Account is
a savings plan open to anyone under the
age of 18. When the account owner
withdraws money to pay for qualified
higher education expenses, the
withdrawals are generally tax-free
(required in the US).
47.4.4.8.16.3.5.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Exemption reason expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification47" on page 4539 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4540
   Issuer <Issr> [1..1] Text 4540
   SchemeName <SchmeNm> [0..1] Text 4540
47.4.4.8.16.3.6  RecipientIdentification <RcptId>
Presence: [0..1]
Approved by the Securities SEG on 27 January 2026 setr.007.001.05 SubscriptionBulkOrderV05
Investment Funds - Maintenance 2025 - 2026 2607 May 2026
```

