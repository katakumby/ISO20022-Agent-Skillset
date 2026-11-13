---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["15 seev.044.001.13 CorporateActionMovementPreliminaryAdviceCancellationAdviceV13", "15.4 Message Building Blocks", "15.4.5 IssuerAgent <IssrAgt>"]
file_pages: [825]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.044.001.13"]
---

# 15.4.5 IssuerAgent <IssrAgt>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 825 to 825.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 825

```text
LotteryType <LtryTp> contains one of the following elements (see "LotteryTypeFormat4Choice" on
page 979 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 979
Or}   Proprietary <Prtry> [1..1] ± 979
15.4.5 IssuerAgent <IssrAgt>
Presence: [0..*]
Definition: Party appointed to administer the event on behalf of the issuer company/offeror. The party
may be contacted for more information about the event.
IssuerAgent <IssrAgt> contains one of the following elements (see "PartyIdentification120Choice" on
page 1045 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AnyBIC <AnyBIC> [1..1] IdentifierSet C1 1045
Or   ProprietaryIdentification <PrtryId> [1..1] ± 1046
Or}   NameAndAddress <NmAndAdr> [1..1] ± 1046
15.4.6 PayingAgent <PngAgt>
Presence: [0..*]
Definition: Agent (principal or fiscal paying agent) appointed to execute the payment for the corporate
action event on behalf of the issuer company/offeror.
PayingAgent <PngAgt> contains one of the following elements (see "PartyIdentification120Choice" on
page 1045 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AnyBIC <AnyBIC> [1..1] IdentifierSet C1 1045
Or   ProprietaryIdentification <PrtryId> [1..1] ± 1046
Or}   NameAndAddress <NmAndAdr> [1..1] ± 1046
15.4.7 SubPayingAgent <SubPngAgt>
Presence: [0..*]
Definition: Sub-agent appointed to execute the payment for the corporate action event on behalf of the
issuer company/offeror.
Approved by the Securities SEG on 27 January 2026 seev.044.001.13
CorporateActionMovementPreliminaryAdviceCancel
lationAdviceV13
Corporate Actions - Maintenance 2025 - 2026 825 February 2026
```

