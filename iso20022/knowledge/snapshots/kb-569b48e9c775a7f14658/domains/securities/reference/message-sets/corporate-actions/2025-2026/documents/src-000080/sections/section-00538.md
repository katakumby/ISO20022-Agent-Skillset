---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["11 seev.039.001.13 CorporateActionCancellationAdviceV13", "11.3 Constraints"]
file_pages: [704]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.039.001.13"]
---

# 11.3 Constraints

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 704 to 704.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 704

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
     LotteryType <LtryTp> [0..1] ± 714
   AdditionalText <AddtlTxt> [0..*] Text 715
   IssuerAgent <IssrAgt> [0..*] ± 715
   PayingAgent <PngAgt> [0..*] ± 715
   SubPayingAgent <SubPngAgt> [0..*] ± 715
   Registrar <Regar> [0..1] ± 716
   ResellingAgent <RsellngAgt> [0..*] ± 716
   PhysicalSecuritiesAgent <PhysSctiesAgt> [0..1] ± 716
   DropAgent <DrpAgt> [0..1] ± 717
   SolicitationAgent <SlctnAgt> [0..*] ± 717
   InformationAgent <InfAgt> [0..1] ± 717
   SupplementaryData <SplmtryData> [0..*] ± C14 718
11.3 Constraints
C1 AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the
ISO directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
C2 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
C3 DescriptionPresenceRule
If Description is not present then either ISIN or at least one occurrence of OtherIdentification
must be present.
C4 DescriptionUsageRule
Description must be used alone as the last resort.
C5 EventTypeRule
If Code is present, the code OTHR (Other) must only be used if no other corporate action event
code is appropriate.
If Code is present, the code CHAN (Change) must only be used if no other corporate action
event code is appropriate and only for an event which relates to a change.
If Code is present, the code REDM (Final Maturity) must only be used if the redemption is
decided by the issuer and not by the securities holders.
Approved by the Securities SEG on 27 January 2026 seev.039.001.13
CorporateActionCancellationAdviceV13
Corporate Actions - Maintenance 2025 - 2026 704 February 2026
```

