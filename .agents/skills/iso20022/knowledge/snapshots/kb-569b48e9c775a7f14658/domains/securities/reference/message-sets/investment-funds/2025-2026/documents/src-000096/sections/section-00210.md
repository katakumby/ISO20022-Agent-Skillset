---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["15 reda.004.001.07 FundReferenceDataReportV07", "15.4 Message Building Blocks", "15.4.5 Report <Rpt>", "15.4.5.4 GeneralReferenceDate <GnlRefDt>"]
file_pages: [309]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.004.001.07"]
---

# 15.4.5.4 GeneralReferenceDate <GnlRefDt>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 309 to 309.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 309

```text
AuthorisedProxy <AuthrsdPrxy> contains the following elements (see "ContactAttributes6" on
page 4964 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [0..1] Text 4964
   PostalAddress <PstlAdr> [0..1] ± 4964
   PhoneNumber <PhneNb> [0..1] Text 4965
   FaxNumber <FaxNb> [0..1] Text 4965
   EmailAddress <EmailAdr> [0..1] Text 4965
   URLAddress <URLAdr> [0..1] Text 4965
   AnyBIC <AnyBIC> [0..1] IdentifierSet C4 4965
   LEI <LEI> [0..1] IdentifierSet 4966
15.4.5.4  GeneralReferenceDate <GnlRefDt>
Presence: [1..1]
Definition: Date to which the data refers. When used in reference to MiFID, this is in the scope of the
European MiFID Template (EMT) reference 00050. 
Datatype: "ISODate" on page 5388
15.4.5.5  TargetMarketIndicator <TrgtMktInd>
Presence: [0..1]
Definition: Indicates whether target market data is included in the report. When used in reference to
MiFID, this is in the scope of the European MiFID Template (EMT) reference 00006.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
15.4.5.6  ExAnteIndicator <ExAnteInd>
Presence: [0..1]
Definition: Indicates whether ex ante costs and charges are included in the report. When used in
reference to MiFID, this is in the scope of the European MiFID Template (EMT) reference 00007.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
15.4.5.7  ExPostIndicator <ExPstInd>
Presence: [0..1]
Definition: Indicates whether ex post costs and charges are included in the report. When used in
reference to MiFID, this is in the scope of the European MiFID Template (EMT) reference 00008.
Approved by the Securities SEG on 27 January 2026 reda.004.001.07 FundReferenceDataReportV07
Investment Funds - Maintenance 2025 - 2026 309 May 2026
```

