---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["32 reda.012.001.01 SecurityReportV01", "32.4 Message Building Blocks", "32.4.3 SecurityReportOrError <SctyRptOrErr>", "32.4.3.1 SecurityReportOrBusinessError <SctyRptOrBizErr>", "32.4.3.1.1 SecurityReport <SctyRpt>", "32.4.3.1.1.2 FinancialInstrumentType <FinInstrmTp>", "32.4.3.1.1.2.2 Warrant <Warrt>", "32.4.3.1.1.2.2.1 Multiplier <Mltplr>"]
file_pages: [1868]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.012.001.01"]
---

# 32.4.3.1.1.2.2.1 Multiplier <Mltplr>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 1868 to 1868.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1868

```text
Warrant <Warrt> contains the following Warrant4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Multiplier <Mltplr> [0..1] Rate 1868
   SubscriptionPrice <SbcptPric> [0..1]  1868
     ValueType <ValTp> [0..1] CodeSet 1869
     Value <Val> [1..1] ± 1869
     PriceType <PricTp> [0..1] CodeSet 1870
   Type <Tp> [0..1]  1870
{Or     Code <Cd> [1..1] CodeSet 1871
Or}     Proprietary <Prtry> [1..1] ± 1871
   WarrantAgent <WarrtAgt> [0..*]  1871
     Name <Nm> [1..1] Text 1872
     Identification <Id> [0..1]  1872
{Or       AnyBIC <AnyBIC> [1..1] IdentifierSet C3 1872
Or}       ProprietaryIdentification <PrtryId> [1..1] ± 1873
     Purpose <Purp> [0..1] Text 1873
     TaxationCountry <TaxtnCtry> [0..1] CodeSet C4 1873
     RegistrationCountry <RegnCtry> [0..1] CodeSet C4 1873
     RegistrationDate <RegnDt> [0..1] Date 1874
     TaxIdentificationNumber <TaxIdNb> [0..1] Text 1874
     NationalRegistrationNumber <NtlRegnNb> [0..1] Text 1874
     PostalAddress <PstlAdr> [1..5] ± C10 1874
     PrimaryCommunicationAddress <PmryComAdr> [0..1] ± 1874
     SecondaryCommunicationAddress <ScndryComAdr> [0..1] ± 1875
32.4.3.1.1.2.2.1  Multiplier <Mltplr>
Presence: [0..1]
Definition: Specifies the ratio or multiply factor used to convert from contracts to shares.
Datatype: "BaseOneRate" on page 3324
32.4.3.1.1.2.2.2  SubscriptionPrice <SbcptPric>
Presence: [0..1]
Definition: Pre-determined price at which the holder of a warrant is entitled to buy the underlying
instrument.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.012.001.01 SecurityReportV01
Target2-Securities 1868 August 2026
```

