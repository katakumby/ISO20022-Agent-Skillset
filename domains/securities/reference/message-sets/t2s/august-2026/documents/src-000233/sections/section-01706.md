---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["63 reda.046.001.01 SecurityCSDLinkMaintenanceRequestV01", "63.4 Message Building Blocks", "63.4.2 SecurityCSDLinkIdentification <SctyCSDLkId>", "63.4.2.1 FinancialInstrumentIdentification <FinInstrmId>"]
file_pages: [2354]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.046.001.01"]
---

# 63.4.2.1 FinancialInstrumentIdentification <FinInstrmId>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2354 to 2354.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2354

```text
SecurityCSDLinkIdentification <SctyCSDLkId> contains the following SecurityCSDLink9 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C3, C4,
C5, C6,
C7
2354
   IssuerInvestorCSD <IssrInvstrCSD> [1..1]  2355
{Or     IssuerCSD <IssrCSD> [1..1]  2355
{Or       OrganisationIdentification <OrgId> [1..1] ± 2356
Or}       CombinedIdentification <CmbndId> [1..1] ± 2356
Or}     InvestorCSD <InvstrCSD> [1..1]  2356
{Or       OrganisationIdentification <OrgId> [1..1] ± 2356
Or}       CombinedIdentification <CmbndId> [1..1] ± 2357
   ValidFrom <VldFr> [1..1] ± 2357
63.4.2.1  FinancialInstrumentIdentification <FinInstrmId>
Presence: [1..1]
Definition: Identification of a security.
Impacted by: C3 "DescriptionPresenceRule", C4 "DescriptionUsageRule", C5 "ISINGuideline", C6
"ISINPresenceRule", C7 "OtherIdentificationPresenceRule"
FinancialInstrumentIdentification <FinInstrmId> contains the following elements (see
"SecurityIdentification19" on page 2951 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ISIN <ISIN> [0..1] IdentifierSet 2952
   OtherIdentification <OthrId> [0..*]  2952
     Identification <Id> [1..1] Text 2952
     Suffix <Sfx> [0..1] Text 2952
     Type <Tp> [1..1] ± 2952
   Description <Desc> [0..1] Text 2953
Constraints
• DescriptionPresenceRule
If Description is not present then either ISIN or at least one occurrence of OtherIdentification must be
present.
On Condition
    /Description is absent
Following Must be True
    /ISIN Must be present
 Or    /OtherIdentification[*] Must be present
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.046.001.01
SecurityCSDLinkMaintenanceRequestV01
Target2-Securities 2354 August 2026
```

