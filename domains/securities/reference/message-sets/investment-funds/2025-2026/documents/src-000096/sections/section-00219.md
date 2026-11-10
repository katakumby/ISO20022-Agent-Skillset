---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["15 reda.004.001.07 FundReferenceDataReportV07", "15.4 Message Building Blocks", "15.4.5 Report <Rpt>", "15.4.5.8 SecurityIdentification <SctyId>", "15.4.5.8.17 QuotationType <QtnTp>"]
file_pages: [319]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.004.001.07"]
---

# 15.4.5.8.17 QuotationType <QtnTp>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 319 to 319.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 319

```text
Proprietary <Prtry> contains the following elements (see "GenericIdentification47" on page 4539 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4540
   Issuer <Issr> [1..1] Text 4540
   SchemeName <SchmeNm> [0..1] Text 4540
15.4.5.8.17  QuotationType <QtnTp>
Presence: [0..1]
Definition: When the financial instrument is a structured security, specifies if the ex-ante and ex-post
costs and charges are specified as an absolute figure, that is, a currency and amount, or as a
percentage rate, related to the specific reference value.
When used in reference to MiFID, this is in the scope of the European MiFID Template reference
00096.
QuotationType <QtnTp> contains one of the following elements (see "QuotationType1Choice" on
page 4512 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4512
Or}   Proprietary <Prtry> [1..1] ± 4512
15.4.5.8.18  LeveragedOrContingentLiability <LvrgdOrCntngntLblty>
Presence: [0..1]
Definition: Indicates whether the financial instrument is leveraged or has contingent liability. This
enables reporting on the depreciation of leveraged financial instruments or contingent liability
transactions in accordance with Art. 62 of the MiFID II's Delegated Regulation as defined in the scope
of European MiFID Template (EMT) reference 00100.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
15.4.5.8.19  NoRetrocessionIndicator <NoRtrcssnInd>
Presence: [0..1]
Definition: Indicates whether the share class does not pay retrocession fees and commissions. When
used in reference to MiFID, this is in the scope of the European MiFID Template (EMT) reference
00110.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
Approved by the Securities SEG on 27 January 2026 reda.004.001.07 FundReferenceDataReportV07
Investment Funds - Maintenance 2025 - 2026 319 May 2026
```

