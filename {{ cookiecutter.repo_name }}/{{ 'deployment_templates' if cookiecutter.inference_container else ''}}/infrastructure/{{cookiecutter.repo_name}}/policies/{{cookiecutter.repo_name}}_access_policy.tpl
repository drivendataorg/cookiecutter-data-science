{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "CommunityToTeamDataAccess",
            "Effect": "Allow",
            "Action": "s3:ListBucket",
            "Resource": "arn:aws:s3:::${ml_{{ cookiecutter.repo_name }}_bucket}"
        },
        {
            "Sid": "",
            "Effect": "Allow",
            "Action": [
                "s3:PutObject",
                "s3:GetObject"
            ],
            "Resource": "arn:aws:s3:::${ml_{{ cookiecutter.repo_name }}_bucket}/predictions/*"
        }
    ]
}