---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["13 Message Items Types", "13.1 MessageComponents", "13.1.6 Financial Instrument", "13.1.6.3 CommonFinancialInstrumentAttributes11", "13.1.6.3.2 FinancialInstrumentName <FinInstrmNm>", "13.1.6.3.2.1 ISOShortName <ISOShrtNm>"]
file_pages: [332]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 13.1.6.3.2.1 ISOShortName <ISOShrtNm>

Source: [src-000378](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 332 to 332.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 332

```text
13.1.6.3.2.1  ISOShortName <ISOShrtNm>
Presence: [0..1]
Definition: Short name of the security expressed as ISO 18773/18774.
Datatype: "Max35Text" on page 534
13.1.6.3.2.2  ISOLongName <ISOLngNm>
Presence: [0..1]
Definition: Name of the security.
Datatype: "Max350Text" on page 534
13.1.6.3.2.3  ValidFrom <VldFr>
Presence: [0..1]
Definition: Defines the date since when the name of the security is valid.
ValidFrom <VldFr> contains one of the following elements (see "DateAndDateTime2Choice" on
page 236 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 236
Or}   DateTime <DtTm> [1..1] DateTime 236
13.1.6.3.3  DenominationCurrency <DnmtnCcy>
Presence: [0..1]
Definition: Currency in which a security is issued or redenominated.
Impacted by: C2 "ActiveOrHistoricCurrency"
Datatype: "ActiveOrHistoricCurrencyCode" on page 508
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
13.1.6.3.4  CertificateNumber <CertNb>
Presence: [0..1]
Definition: Unique and unambiguous identifier of a certificate assigned by the issuer.
Datatype: "Max35Text" on page 534
13.1.6.3.5  ContractVersionNumber <CtrctVrsnNb>
Presence: [0..1]
Definition: Version number assigned to the contract associated with the security.
Datatype: "Number" on page 532
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
Message Items Types
Target2-Securities - Securities Reference Data 332 March 2024
```

