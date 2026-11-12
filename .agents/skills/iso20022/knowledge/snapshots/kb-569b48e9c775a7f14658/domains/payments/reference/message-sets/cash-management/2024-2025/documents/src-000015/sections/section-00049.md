---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["3 camt.004.001.10 ReturnAccountV10", "3.4 Message Building Blocks", "3.4.2 ReportOrError <RptOrErr>", "3.4.2.1 AccountReport <AcctRpt>", "3.4.2.1.2 AccountOrError <AcctOrErr>", "3.4.2.1.2.1 Account <Acct>", "3.4.2.1.2.1.10 StandingOrder <StgOrdr>", "3.4.2.1.2.1.10.5 AssociatedPoolAccount <AssoctdPoolAcct>"]
file_pages: [84]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.004.001.10"]
---

# 3.4.2.1.2.1.10.5 AssociatedPoolAccount <AssoctdPoolAcct>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 84 to 84.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 84

```text
3.4.2.1.2.1.10.5  AssociatedPoolAccount <AssoctdPoolAcct>
Presence: [0..1]
Definition: Liquidity transfer origin or destination account within the pool of accounts under management
of the requestor.
AssociatedPoolAccount <AssoctdPoolAcct> contains one of the following elements (see
"AccountIdentification4Choice" on page 787 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   IBAN <IBAN> [1..1] IdentifierSet C5 787
Or}   Other <Othr> [1..1] ± 788
3.4.2.1.2.1.10.6  Reference <Ref>
Presence: [0..1]
Definition: Unique and unambiguous identification for a standing order, as assigned by the account
servicer or the account owner.
Datatype: "Max35Text" on page 889
3.4.2.1.2.1.10.7  Frequency <Frqcy>
Presence: [0..1]
Definition: Regularity with which payment instructions are to be created and processed as a result of the
standing order, such as daily, weekly, or monthly.
Datatype: "Frequency2Code" on page 858
CodeName Name Definition
YEAR Annual Event takes place every year or once a
year.
MNTH Monthly Event takes place every month or once a
month.
QURT Quarterly Event takes place every three months or
four times a year.
MIAN SemiAnnual Event takes place every six months or
two times a year.
WEEK Weekly Event takes place once a week.
DAIL Daily Event takes place every day.
ADHO Adhoc Event takes place on request or as
necessary.
INDA IntraDay Event takes place several times a day.
OVNG Overnight Event takes place overnight.
3.4.2.1.2.1.10.8  ValidityPeriod <VldtyPrd>
Presence: [0..1]
Definition: Dates during which the standing order is in effect.
Approved by the Payments SEG on 04 February 2025 camt.004.001.10 ReturnAccountV10
Cash Management - Maintenance 2024 - 2025 84 February 2025
```

