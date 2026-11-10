---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["33 sese.010.001.07 TransferCancellationStatusReportV07", "34.4 Message Building Blocks", "34.4.4 StatusReport <StsRpt>", "34.4.4.17 Conversion <Convs>", "34.4.4.17.3 UnitsDetails <UnitsDtls>", "34.4.4.17.3.1 Units <Units>"]
file_pages: [891]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.011.001.10"]
---

# 34.4.4.17.3.1 Units <Units>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 891 to 891.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 891

```text
UnitsDetails <UnitsDtls> contains the following Unit15 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Units <Units> [1..1]  891
{Or     UnitsNumber <UnitsNb> [1..1] Quantity 891
Or}     DigitalTokenUnit <DgtlTknUnit> [1..1] Quantity 891
   OrderDate <OrdrDt> [0..1] Date 891
   AcquisitionDate <AcqstnDt> [0..1] Date 891
   CertificateNumber <CertNb> [0..*] Text 892
   Group1Or2Units <Grp1Or2Units> [0..1] CodeSet 892
   Reference <Ref> [0..1] Text 892
34.4.4.17.3.1  Units <Units>
Presence: [1..1]
Definition: Quantity of units or digital tokens.
Units <Units> contains one of the following Unit1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   UnitsNumber <UnitsNb> [1..1] Quantity 891
Or}   DigitalTokenUnit <DgtlTknUnit> [1..1] Quantity 891
34.4.4.17.3.1.1  UnitsNumber <UnitsNb>
Presence: [1..1]
Definition: Quantity of units.
Datatype: "DecimalNumber" on page 5400
34.4.4.17.3.1.2  DigitalTokenUnit <DgtlTknUnit>
Presence: [1..1]
Definition: Quantity of digital tokens expressed as a number, for example, a number of blockchain
tokens.
Datatype: "Max30DecimalNumber" on page 5400
34.4.4.17.3.2  OrderDate <OrdrDt>
Presence: [0..1]
Definition: Date the investor or its agent placed the original order.
Datatype: "ISODate" on page 5388
34.4.4.17.3.3  AcquisitionDate <AcqstnDt>
Presence: [0..1]
Definition: Date the investor purchased the financial instrument.
Approved by the Securities SEG on 27 January 2026 sese.011.001.10
TransferInstructionStatusReportV10
Investment Funds - Maintenance 2025 - 2026 891 May 2026
```

