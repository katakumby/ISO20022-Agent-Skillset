---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["33 sese.010.001.07 TransferCancellationStatusReportV07", "33.2 Structure"]
file_pages: [810]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.010.001.07"]
---

# 33.2 Structure

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 810 to 810.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 810

```text
Identifies the market practice to which the message conforms.
F. Extension
Additional information that cannot be captured in the structured elements and/or any other specific
block.
33.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <TrfCxlStsRpt> [1..1]  C4, C5
   MessageIdentification <MsgId> [1..1] ± 811
   CounterpartyReference <CtrPtyRef> [0..1] ± 811
   Reference <Ref> [0..1] ± 812
   StatusReport <StsRpt> [1..1]  812
     MasterReference <MstrRef> [0..1] Text 812
     TransferReference <TrfRef> [1..1] Text 812
     ClientReference <ClntRef> [0..1] ± 813
     CancellationReference <CxlRef> [0..1] Text 813
     Status <Sts> [1..1]  813
{Or       Status <Sts> [1..1] ± 813
Or       Rejected <Rjctd> [1..1] ± 814
Or       Complete <Cmplt> [1..1] ± 814
Or}       Pending <Pdg> [1..1] ± 814
     StatusInitiator <StsInitr> [0..1] ± 814
   MarketPracticeVersion <MktPrctcVrsn> [0..1] ± 815
   Extension <Xtnsn> [0..*] ± C3 815
33.3 Constraints
C1 AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the
ISO directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
C2 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
Approved by the Securities SEG on 27 January 2026 sese.010.001.07
TransferCancellationStatusReportV07
Investment Funds - Maintenance 2025 - 2026 810 May 2026
```

