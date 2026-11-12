---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["41 reda.021.001.01 SecuritiesAccountReportV01", "41.4 Message Building Blocks", "41.4.3 ReportOrError <RptOrErr>", "41.4.3.1 SecuritiesAccountReport <SctiesAcctRpt>", "41.4.3.1.2 SecuritiesAccountOrError <SctiesAcctOrErr>", "41.4.3.1.2.1 SecuritiesAccount <SctiesAcct>", "41.4.3.1.2.1.4 NegativePosition <NegPos>"]
file_pages: [2134]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.021.001.01"]
---

# 41.4.3.1.2.1.4 NegativePosition <NegPos>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2134 to 2134.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2134

```text
Usage:
- Meaning when true: account is in hold status.
- Meaning when false: account is in release status.
Datatype: One of the following values must be used (see "TrueFalseIndicator" on page 3323):
• Meaning When True: True
• Meaning When False: False
41.4.3.1.2.1.4  NegativePosition <NegPos>
Presence: [0..1]
Definition: Indicates whether the securities account can hold a negative position in a security or not.
Datatype: One of the following values must be used (see "TrueFalseIndicator" on page 3323):
• Meaning When True: True
• Meaning When False: False
41.4.3.1.2.1.5  Type <Tp>
Presence: [0..1]
Definition: Specifies the type of the securities account.
Type <Tp> contains one of the following SystemSecuritiesAccountType1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 2134
Or}   Proprietary <Prtry> [1..1] ± 2135
41.4.3.1.2.1.5.1  Code <Cd>
Presence: [1..1]
Definition: System securities account type, in a coded form.
Datatype: "SystemSecuritiesAccountType1Code" on page 3305
CodeName Name Definition
CSDP CSDParticipantAccount Account owned by a CSD Participant
.
CSDM CSDMirrorAccount Account operated by CSD for mirroring
positions
.
ICSA InterCSDAccount Account operated by CSD for settlement
of securities legs for instructions
involving internal CSD s.
TOFF TechnicalOffsetAccount Account operated by CSDs in a direct
holding market context.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.021.001.01 SecuritiesAccountReportV01
Target2-Securities 2134 August 2026
```

