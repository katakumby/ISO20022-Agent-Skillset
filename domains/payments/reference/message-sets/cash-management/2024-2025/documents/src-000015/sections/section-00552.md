---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["31 camt.070.001.06 ReturnStandingOrderV06", "31.4 Message Building Blocks", "31.4.2 ReportOrError <RptOrErr>", "31.4.2.1 Report <Rpt>", "31.4.2.1.2 StandingOrderOrError <StgOrdrOrErr>", "31.4.2.1.2.1 StandingOrder <StgOrdr>", "31.4.2.1.2.1.5 AssociatedPoolAccount <AssoctdPoolAcct>"]
file_pages: [724]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.070.001.06"]
---

# 31.4.2.1.2.1.5 AssociatedPoolAccount <AssoctdPoolAcct>

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 724 to 724.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 724

```text
31.4.2.1.2.1.5  AssociatedPoolAccount <AssoctdPoolAcct>
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
31.4.2.1.2.1.6  Reference <Ref>
Presence: [0..1]
Definition: Unique and unambiguous identification for a standing order, as assigned by the account
servicer or the account owner.
Datatype: "Max35Text" on page 889
31.4.2.1.2.1.7  Frequency <Frqcy>
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
31.4.2.1.2.1.8  ValidityPeriod <VldtyPrd>
Presence: [0..1]
Definition: Dates during which the standing order is in effect.
Approved by the Payments SEG on 04 February 2025 camt.070.001.06 ReturnStandingOrderV06
Cash Management - Maintenance 2024 - 2025 724 February 2025
```

