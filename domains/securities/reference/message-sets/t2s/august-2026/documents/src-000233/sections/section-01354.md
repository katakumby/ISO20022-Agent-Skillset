---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["32 reda.012.001.01 SecurityReportV01", "32.4 Message Building Blocks", "32.4.3 SecurityReportOrError <SctyRptOrErr>", "32.4.3.1 SecurityReportOrBusinessError <SctyRptOrBizErr>", "32.4.3.1.1 SecurityReport <SctyRpt>", "32.4.3.1.1.3 FinancialInstrumentAttributes <FinInstrmAttrbts>", "32.4.3.1.1.3.2 FinancialInstrumentName <FinInstrmNm>"]
file_pages: [1963]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.012.001.01"]
---

# 32.4.3.1.1.3.2 FinancialInstrumentName <FinInstrmNm>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 1963 to 1963.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1963

```text
32.4.3.1.1.3.2  FinancialInstrumentName <FinInstrmNm>
Presence: [0..*]
Definition: Name of the security.
FinancialInstrumentName <FinInstrmNm> contains the following FinancialInstrumentName2
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ISOShortName <ISOShrtNm> [0..1] Text 1963
   ISOLongName <ISOLngNm> [0..1] Text 1963
   ValidFrom <VldFr> [0..1] ± 1963
32.4.3.1.1.3.2.1  ISOShortName <ISOShrtNm>
Presence: [0..1]
Definition: Short name of the security expressed as ISO 18773/18774.
Datatype: "Max35Text" on page 3328
32.4.3.1.1.3.2.2  ISOLongName <ISOLngNm>
Presence: [0..1]
Definition: Name of the security.
Datatype: "Max350Text" on page 3328
32.4.3.1.1.3.2.3  ValidFrom <VldFr>
Presence: [0..1]
Definition: Defines the date since when the name of the security is valid.
ValidFrom <VldFr> contains one of the following elements (see "DateAndDateTime2Choice" on
page 2914 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 2914
Or}   DateTime <DtTm> [1..1] DateTime 2914
32.4.3.1.1.3.3  DenominationCurrency <DnmtnCcy>
Presence: [0..1]
Definition: Currency in which a security is issued or redenominated.
Impacted by: C2 "ActiveOrHistoricCurrency"
Datatype: "ActiveOrHistoricCurrencyCode" on page 3212
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.012.001.01 SecurityReportV01
Target2-Securities 1963 August 2026
```

