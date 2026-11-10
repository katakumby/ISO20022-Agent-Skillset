---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["27 reda.006.001.01 SecurityCreationRequestV01", "27.4 Message Building Blocks", "27.4.2 Security <Scty>", "27.4.2.2 FinancialInstrumentType <FinInstrmTp>", "27.4.2.2.2 Warrant <Warrt>", "27.4.2.2.2.1 Multiplier <Mltplr>"]
file_pages: [666]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.006.001.01"]
---

# 27.4.2.2.2.1 Multiplier <Mltplr>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 666 to 666.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 666

```text
Warrant <Warrt> contains the following Warrant4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Multiplier <Mltplr> [0..1] Rate 666
   SubscriptionPrice <SbcptPric> [0..1]  666
     ValueType <ValTp> [0..1] CodeSet 667
     Value <Val> [1..1] ± 667
     PriceType <PricTp> [0..1] CodeSet 668
   Type <Tp> [0..1]  668
{Or     Code <Cd> [1..1] CodeSet 669
Or}     Proprietary <Prtry> [1..1] ± 669
   WarrantAgent <WarrtAgt> [0..*]  669
     Name <Nm> [1..1] Text 670
     Identification <Id> [0..1]  670
{Or       AnyBIC <AnyBIC> [1..1] IdentifierSet C3 670
Or}       ProprietaryIdentification <PrtryId> [1..1] ± 671
     Purpose <Purp> [0..1] Text 671
     TaxationCountry <TaxtnCtry> [0..1] CodeSet C4 671
     RegistrationCountry <RegnCtry> [0..1] CodeSet C4 671
     RegistrationDate <RegnDt> [0..1] Date 672
     TaxIdentificationNumber <TaxIdNb> [0..1] Text 672
     NationalRegistrationNumber <NtlRegnNb> [0..1] Text 672
     PostalAddress <PstlAdr> [1..5] ± C10 672
     PrimaryCommunicationAddress <PmryComAdr> [0..1] ± 672
     SecondaryCommunicationAddress <ScndryComAdr> [0..1] ± 673
27.4.2.2.2.1  Multiplier <Mltplr>
Presence: [0..1]
Definition: Specifies the ratio or multiply factor used to convert from contracts to shares.
Datatype: "BaseOneRate" on page 3324
27.4.2.2.2.2  SubscriptionPrice <SbcptPric>
Presence: [0..1]
Definition: Pre-determined price at which the holder of a warrant is entitled to buy the underlying
instrument.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.006.001.01 SecurityCreationRequestV01
Target2-Securities 666 August 2026
```

