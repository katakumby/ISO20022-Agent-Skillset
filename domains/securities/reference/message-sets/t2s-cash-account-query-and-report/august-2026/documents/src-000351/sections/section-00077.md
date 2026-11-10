---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CashAccountQueryAndReport"
source_ids: ["src-000351"]
source_editions: ["august-2026"]
message_ids: []
heading_path: ["3 acmt.026.001.02 AccountListReportV02", "3.4 Message Building Blocks", "3.4.4 ReportOrError <RptOrErr>", "3.4.4.2 AccountReport <AcctRpt>", "3.4.4.2.4 Mandate <Mndt>", "3.4.4.2.4.2 ApplicableChannel <AplblChanl>"]
file_pages: [91]
content_origin: "source-text-extraction"
mentioned_message_ids: ["acmt.026.001.02"]
---

# 3.4.4.2.4.2 ApplicableChannel <AplblChanl>

Source: [src-000351](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CashAccountQueryAndReport_MessageSet/ISO20022_MDRPart2_Target2Securities_CashAccountQueryAndReport_v1.pdf`. Locator: one-based file pages 91 to 91.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 91

```text
3.4.4.2.4.2  ApplicableChannel <AplblChanl>
Presence: [1..*]
Definition: Channel for which the operation mandate is valid. If ApplicableChannel equals Fax, this
means that a bank operation instruction sent by fax will be processed according to the mandates
exchanged in this message.
ApplicableChannel <AplblChanl> contains one of the following Channel2Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 91
Or}   Proprietary <Prtry> [1..1] Text 91
3.4.4.2.4.2.1  Code <Cd>
Presence: [1..1]
Definition: Specifies a channel by means of a code.
Datatype: "CommunicationMethod3Code" on page 174
CodeName Name Definition
EMAL Email Transmission by e-mail.
FAXI Fax Transmission by fax.
POST PostalService Transmission by postal service.
PHON Phone Transmission by telephone.
FILE File Transmission by file transfer.
ONLI Online Transmission on line, for example, in a
web portal.
3.4.4.2.4.2.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Specifies a channel by means of a text.
Datatype: "Max35Text" on page 183
3.4.4.2.4.3  RequiredSignatureNumber <ReqrdSgntrNb>
Presence: [1..1]
Definition: Number of required and necessary signatures by the mandate.
Datatype: "Max15PlusSignedNumericText" on page 182
3.4.4.2.4.4  SignatureOrderIndicator <SgntrOrdrInd>
Presence: [1..1]
Definition: Indicator whether a certain order of signatures has to be respected or not.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 181):
• Meaning When True: Yes
• Meaning When False: No
Approved by the Securities Standards Evaluation Group (SEG) on 18 June
2026.
acmt.026.001.02 AccountListReportV02
Target2-Securities - Cash Account Query and Report 91 August 2026
```

