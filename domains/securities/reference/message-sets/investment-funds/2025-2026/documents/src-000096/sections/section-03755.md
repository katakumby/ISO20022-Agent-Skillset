---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.30 Party Identification", "66.1.30.44 KYCCheckType1Choice"]
file_pages: [5042]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.30.44 KYCCheckType1Choice

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 5042 to 5042.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5042

```text
ContactPerson <CtctPrsn> contains the following elements (see "ContactIdentification2" on
page 5095 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   NamePrefix <NmPrfx> [0..1] CodeSet 5095
   GivenName <GvnNm> [0..1] Text 5095
   Name <Nm> [1..1] Text 5096
   PhoneNumber <PhneNb> [0..1] Text 5096
   MobileNumber <MobNb> [0..1] Text 5096
   FaxNumber <FaxNb> [0..1] Text 5096
   EmailAddress <EmailAdr> [0..1] Text 5096
66.1.30.44  KYCCheckType1Choice
Definition: Choice of formats for the specification of the Know Your Customer (KYC) check type.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 5042
Or}   Proprietary <Prtry> [1..1] ± 5042
66.1.30.44.1  Code <Cd>
Presence: [1..1]
Definition: Type of Know Your Customer (KYC) check type expressed as a code.
Datatype: "KnowYourCustomerCheckType1Code" on page 5328
CodeName Name Definition
ENHA Enhanced Enhanced check, typically carried out on
accounts that are considered high risk.
ORDN Ordinary Ordinary check, typically carried out on
standard accounts.
SIMP Simple Simple check, typically carried out on
accounts that have a low risk of anti-
money laundering, such as an account
owned by a financial institution.
66.1.30.44.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Type of Know Your Customer (KYC) check type expressed as a proprietary code.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5042 May 2026
```

