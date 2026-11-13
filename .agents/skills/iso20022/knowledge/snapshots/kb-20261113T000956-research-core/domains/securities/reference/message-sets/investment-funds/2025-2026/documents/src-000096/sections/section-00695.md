---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["33 sese.010.001.07 TransferCancellationStatusReportV07", "34.4 Message Building Blocks", "34.4.4 StatusReport <StsRpt>", "34.4.4.21 DrawdownTranche <DrwdwnTrch>", "34.4.4.21.17 AdditionalInformation <AddtlInf>"]
file_pages: [937]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.011.001.10"]
---

# 34.4.4.21.17 AdditionalInformation <AddtlInf>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 937 to 937.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 937

```text
34.4.4.21.17  AdditionalInformation <AddtlInf>
Presence: [0..*]
Definition: Additional information about the drawdown.
AdditionalInformation <AddtlInf> contains the following elements (see "AdditionalInformation15" on
page 4508 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   InformationType <InfTp> [1..1] ± 4508
   InformationValue <InfVal> [1..1] Text 4508
34.4.4.22  OtherDrawdownInformation <OthrDrwdwnInf>
Presence: [0..1]
Definition: Drawdown information not specifically associated with a drawdown tranche.
OtherDrawdownInformation <OthrDrwdwnInf> contains the following Drawdown3 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   EmploymentDetails <MplymntDtls> [0..1]  937
     TaxCode <TaxCd> [0..1] ± 938
     OtherTaxCodeIndicator <OthrTaxCdInd> [0..1] Indicator 938
     CumulativeTaxIndicator <CmltvTaxInd> [0..1] Indicator 938
     PreviousPay <PrvsPay> [0..1] Amount C1, C10 939
     PreviousTax <PrvsTax> [0..1] Amount C1, C10 939
     StartDate <StartDt> [0..1] ± 939
     EndDate <EndDt> [0..1] ± 940
     AdditionalInformation <AddtlInf> [0..*] ± 940
   AdditionalInformation <AddtlInf> [0..*] ± 940
34.4.4.22.1  EmploymentDetails <MplymntDtls>
Presence: [0..1]
Definition: Previous employment information.
Approved by the Securities SEG on 27 January 2026 sese.011.001.10
TransferInstructionStatusReportV10
Investment Funds - Maintenance 2025 - 2026 937 May 2026
```

