---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S LinkReferenceData"
source_ids: ["src-000366"]
source_editions: ["december-2024"]
message_ids: []
heading_path: ["3 reda.046.001.01 SecurityCSDLinkMaintenanceRequestV01", "3.4 Message Building Blocks", "3.4.2 SecurityCSDLinkIdentification <SctyCSDLkId>", "3.4.2.1 FinancialInstrumentIdentification <FinInstrmId>"]
file_pages: [20]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.046.001.01"]
---

# 3.4.2.1 FinancialInstrumentIdentification <FinInstrmId>

Source: [src-000366](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LinkReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_LinkReferenceData_v1.pdf`. Locator: one-based file pages 20 to 20.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 20

```text
SecurityCSDLinkIdentification <SctyCSDLkId> contains the following SecurityCSDLink9 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C3, C4,
C5, C6,
C7
20
   IssuerInvestorCSD <IssrInvstrCSD> [1..1]  21
{Or     IssuerCSD <IssrCSD> [1..1]  21
{Or       OrganisationIdentification <OrgId> [1..1] ± 22
Or}       CombinedIdentification <CmbndId> [1..1] ± 22
Or}     InvestorCSD <InvstrCSD> [1..1]  22
{Or       OrganisationIdentification <OrgId> [1..1] ± 22
Or}       CombinedIdentification <CmbndId> [1..1] ± 23
   ValidFrom <VldFr> [1..1] ± 23
3.4.2.1  FinancialInstrumentIdentification <FinInstrmId>
Presence: [1..1]
Definition: Identification of a security.
Impacted by: C3 "DescriptionPresenceRule", C4 "DescriptionUsageRule", C5 "ISINGuideline", C6
"ISINPresenceRule", C7 "OtherIdentificationPresenceRule"
FinancialInstrumentIdentification <FinInstrmId> contains the following elements (see
"SecurityIdentification19" on page 61 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ISIN <ISIN> [0..1] IdentifierSet 62
   OtherIdentification <OthrId> [0..*]  62
     Identification <Id> [1..1] Text 62
     Suffix <Sfx> [0..1] Text 62
     Type <Tp> [1..1] ± 63
   Description <Desc> [0..1] Text 63
Constraints
• DescriptionPresenceRule
If Description is not present then either ISIN or at least one occurrence of OtherIdentification must be
present.
On Condition
    /Description is absent
Following Must be True
    /ISIN Must be present
 Or    /OtherIdentification[*] Must be present
Approved by the Securities SEG on 21 November 2024. reda.046.001.01
SecurityCSDLinkMaintenanceRequestV01
Target2-Securities - Link Reference Data 20 December 2024
```

