---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.24 Investment Account", "66.1.24.15 InvestmentAccount25"]
file_pages: [4662]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.24.15 InvestmentAccount25

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4662 to 4662.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4662

```text
FiscalYear <FsclYr> contains one of the following elements (see "FiscalYear1Choice" on page 4467
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   StartDate <StartDt> [1..1] Date 4467
Or}   EndDate <EndDt> [1..1] Date 4468
66.1.24.15  InvestmentAccount25
Definition: Account between an investor(s) and a fund manager or a fund. The account can contain
holdings in any investment fund or investment fund class managed (or distributed) by the fund
manager, within the same fund family.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 4662
   Name <Nm> [0..1] Text 4662
   Designation <Dsgnt> [0..1] Text 4662
   IntermediaryInformation <IntrmyInf> [0..10] ± 4663
   AccountServicer <AcctSvcr> [0..1] ± 4663
66.1.24.15.1  Identification <Id>
Presence: [1..1]
Definition: Unique and unambiguous identification for the account between the account owner and the
account servicer.
Identification <Id> contains the following elements (see "AccountIdentification1" on page 4328 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Proprietary <Prtry> [1..1] ± 4329
66.1.24.15.2  Name <Nm>
Presence: [0..1]
Definition: Name of the account. It provides an additional means of identification, and is designated by
the account servicer in agreement with the account owner.
Datatype: "Max35Text" on page 5403
66.1.24.15.3  Designation <Dsgnt>
Presence: [0..1]
Definition: Supplementary registration information applying to a specific block of units for dealing and
reporting purposes. The supplementary registration information may be used when all the units are
registered, for example, to a funds supermarket, but holdings for each investor have to reconciled
individually.
Datatype: "Max35Text" on page 5403
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4662 May 2026
```

