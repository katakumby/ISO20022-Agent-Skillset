---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["28 reda.007.001.01 SecurityMaintenanceRequestV01", "28.4 Message Building Blocks", "28.4.2 UpdateType <UpdTp>", "28.4.2.2 Replace <Rplc>", "28.4.2.2.1 FinancialInstrumentType <FinInstrmTp>", "28.4.2.2.1.2 Warrant <Warrt>", "28.4.2.2.1.2.1 Multiplier <Mltplr>"]
file_pages: [1590]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.007.001.01"]
---

# 28.4.2.2.1.2.1 Multiplier <Mltplr>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 1590 to 1590.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1590

```text
Warrant <Warrt> contains the following Warrant4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Multiplier <Mltplr> [0..1] Rate 1590
   SubscriptionPrice <SbcptPric> [0..1]  1590
     ValueType <ValTp> [0..1] CodeSet 1591
     Value <Val> [1..1] ± 1591
     PriceType <PricTp> [0..1] CodeSet 1592
   Type <Tp> [0..1]  1592
{Or     Code <Cd> [1..1] CodeSet 1593
Or}     Proprietary <Prtry> [1..1] ± 1593
   WarrantAgent <WarrtAgt> [0..*]  1593
     Name <Nm> [1..1] Text 1594
     Identification <Id> [0..1]  1594
{Or       AnyBIC <AnyBIC> [1..1] IdentifierSet C3 1594
Or}       ProprietaryIdentification <PrtryId> [1..1] ± 1595
     Purpose <Purp> [0..1] Text 1595
     TaxationCountry <TaxtnCtry> [0..1] CodeSet C4 1595
     RegistrationCountry <RegnCtry> [0..1] CodeSet C4 1595
     RegistrationDate <RegnDt> [0..1] Date 1596
     TaxIdentificationNumber <TaxIdNb> [0..1] Text 1596
     NationalRegistrationNumber <NtlRegnNb> [0..1] Text 1596
     PostalAddress <PstlAdr> [1..5] ± C10 1596
     PrimaryCommunicationAddress <PmryComAdr> [0..1] ± 1596
     SecondaryCommunicationAddress <ScndryComAdr> [0..1] ± 1597
28.4.2.2.1.2.1  Multiplier <Mltplr>
Presence: [0..1]
Definition: Specifies the ratio or multiply factor used to convert from contracts to shares.
Datatype: "BaseOneRate" on page 3324
28.4.2.2.1.2.2  SubscriptionPrice <SbcptPric>
Presence: [0..1]
Definition: Pre-determined price at which the holder of a warrant is entitled to buy the underlying
instrument.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1590 August 2026
```

