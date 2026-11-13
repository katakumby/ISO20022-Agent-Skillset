---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.24 Investment Account", "66.1.24.4 InvestmentAccountOwnershipInformation17", "66.1.24.4.3 ModifiedInvestorProfileValidation <ModfdInvstrPrflVldtn>", "66.1.24.4.3.2 InvestorProfileValidation <InvstrPrflVldtn>", "66.1.24.4.3.2.4 ResponsibleParty <RspnsblPty>"]
file_pages: [4583]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.24.4.3.2.4 ResponsibleParty <RspnsblPty>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4583 to 4583.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4583

```text
66.1.24.4.3.2.4  ResponsibleParty <RspnsblPty>
Presence: [0..1]
Definition: Identification of the person who is responsible for the document.
Datatype: "Max140Text" on page 5402
66.1.24.4.3.2.5  CertificateType <CertTp>
Presence: [0..1]
Definition: Type of certificate.
CertificateType <CertTp> contains one of the following elements (see "CertificationType1Choice" on
page 5019 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 5019
Or}   Proprietary <Prtry> [1..1] ± 5020
66.1.24.4.3.2.6  CheckingDate <ChckngDt>
Presence: [0..1]
Definition: Date at which the certification check has been performed.
Datatype: "ISODate" on page 5388
66.1.24.4.3.2.7  CheckingFrequency <ChckngFrqcy>
Presence: [0..1]
Definition: Specifies how frequently the check is performed.
Datatype: "EventFrequency1Code" on page 5297
CodeName Name Definition
YEAR Annual Event takes place every year or once a
year.
SEMI SemiAnnual Event takes place every six months or
two times a year.
QUTR Quarterly Event takes place every three months or
four times a year.
TOMN EveryTwoMonths Event takes place every two months.
MNTH Monthly Event takes place every month or once a
month.
TWMN TwiceAMonth Event takes place two times a month.
TOWK EveryTwoWeeks Event takes place every two weeks.
WEEK Weekly Event takes place once a week.
DAIL Daily Event takes place every day.
ADHO Adhoc Event takes place as necessary.
INDA IntraDay Event takes place several times a day.
OVNG Overnight Event takes place overnight.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4583 May 2026
```

