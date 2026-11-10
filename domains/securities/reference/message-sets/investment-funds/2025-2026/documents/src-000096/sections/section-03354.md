---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.24 Investment Account", "66.1.24.4 InvestmentAccountOwnershipInformation17", "66.1.24.4.32 ControllingParty <CtrlgPty>"]
file_pages: [4595]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.24.4.32 ControllingParty <CtrlgPty>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4595 to 4595.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4595

```text
66.1.24.4.32  ControllingParty <CtrlgPty>
Presence: [0..1]
Definition: Party is the controlling person.
(For an Entity that is a legal person, the term "Controlling Persons" means the natural person(s) who
exercises control over the Entity. "Control" over an Entity is generally exercised by the natural person(s)
who ultimately has a controlling ownership interest in the Entity. A "control ownership interest" depends
on the ownership structure of the legal person and is usually identified on the basis of a threshold
applying a risk-based approach (e.g. any person(s) owning more than a certain percentage of the legal
person, such as 25%). Where no natural person(s) exercises control through ownership interests, the
Controlling Person(s) of the Entity will be the natural person(s) who exercises control of the Entity
through other means. Where no natural person(s) is identified as exercising control of the Entity, the
Controlling Person(s) of the Entity will be the natural person(s) who holds the position of senior
managing official.).
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
66.1.24.5  InvestmentAccountCategory1Choice
Definition: Choice of formats for the specification of the category of investment account.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4595
Or}   Proprietary <Prtry> [1..1] ± 4595
66.1.24.5.1  Code <Cd>
Presence: [1..1]
Definition: Category of investment account expressed as a code.
Datatype: "InvestmentAccountCategory1Code" on page 5311
CodeName Name Definition
MAND MandateAccount Account is fully managed by the financial
institution, that is, an investor gives a
'mandate' to the financial institution to
execute a mutually agreed investment
strategy on its behalf.
RETA RetailAccount Account is a standard account managed
by the investor. The investor issues
instructions for the account to the
financial institution.
66.1.24.5.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Category of investment account expressed as a proprietary code.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4595 May 2026
```

